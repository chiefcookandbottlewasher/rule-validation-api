from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rule(db.Model):
    """Represents a rule in the rule validation system."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    condition = db.Column(db.Text)
    action = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return f'<Rule {self.name}>'