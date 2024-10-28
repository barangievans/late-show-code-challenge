from flask import jsonify, request
from app.models import Episode, Guest, Appearance  # Ensure the models are imported
from app import db  # Import your db instance

def configure_routes(app):
    @app.route('/episodes', methods=['GET'])
    def get_episodes():
        """Fetch all episodes."""
        episodes = Episode.query.all()
        return jsonify([episode.to_dict() for episode in episodes])

    @app.route('/episodes/<int:id>', methods=['GET'])
    def get_episode(id):
        """Fetch a specific episode by ID."""
        episode = Episode.query.get(id)
        if episode:
            return jsonify(episode.to_dict())
        return jsonify({"error": "Episode not found"}), 404

    @app.route('/guests', methods=['GET'])
    def get_guests():
        """Fetch all guests."""
        guests = Guest.query.all()
        return jsonify([guest.to_dict() for guest in guests])

    @app.route('/appearances', methods=['GET'])
    def get_appearances():
        """Fetch all appearances."""
        appearances = Appearance.query.all()
        return jsonify([appearance.to_dict() for appearance in appearances])

    @app.route('/appearances/<int:id>', methods=['GET'])
    def get_appearance(id):
        """Fetch a specific appearance by ID."""
        appearance = Appearance.query.get(id)
        if appearance:
            return jsonify(appearance.to_dict())
        return jsonify({"error": "Appearance not found"}), 404

    @app.route('/appearances', methods=['POST'])
    def create_appearance():
        """Create a new appearance."""
        data = request.get_json()
        rating = data.get('rating')
        episode_id = data.get('episode_id')
        guest_id = data.get('guest_id')

        # Validate inputs here, e.g. check if rating is between 1 and 5
        if not (1 <= rating <= 5):
            return jsonify({"error": "Rating must be between 1 and 5"}), 400
        
        new_appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
        db.session.add(new_appearance)
        db.session.commit()

        return jsonify(new_appearance.to_dict()), 201
