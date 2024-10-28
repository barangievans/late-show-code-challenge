from app import app, db  # Ensure db is imported from app after initializing it
from app.models import Episode, Guest, Appearance  # Absolute import

# Sample data
episodes = [
    {
        "number": 1,
        "date": "1999-01-11"
    },
    {
        "number": 2,
        "date": "1999-01-12"
    },
]

guests = [
    {
        "name": "Michael J. Fox",
        "occupation": "actor"
    },
    {
        "name": "Sandra Bernhard",
        "occupation": "comedian"
    },
    {
        "name": "Tracey Ullman",
        "occupation": "television actress"
    }
]

appearances = [
    {
        "rating": 4,
        "episode_number": 1,
        "guest_name": "Michael J. Fox"
    },
    {
        "rating": 5,
        "episode_number": 2,
        "guest_name": "Tracey Ullman"
    }
]

# Function to add sample data to the database
def seed_data():
    with app.app_context():
        # Drop all tables and create new ones
        db.drop_all()
        db.create_all()

        # Add Episodes
        for ep in episodes:
            episode = Episode(number=ep["number"], date=ep["date"])
            db.session.add(episode)

        # Add Guests
        for guest in guests:
            new_guest = Guest(name=guest["name"], occupation=guest["occupation"])
            db.session.add(new_guest)

        # Commit Episodes and Guests first
        db.session.commit()

        # Add Appearances
        for appearance in appearances:
            episode = Episode.query.filter_by(number=appearance["episode_number"]).first()
            guest = Guest.query.filter_by(name=appearance["guest_name"]).first()
            if episode and guest:
                new_appearance = Appearance(
                    rating=appearance["rating"],
                    episode_id=episode.id,
                    guest_id=guest.id
                )
                db.session.add(new_appearance)

        # Commit all changes
        db.session.commit()

if __name__ == "__main__":
    seed_data()
    print("Database seeded successfully!")
