class Poem:
    def __init__(self, title, poet, poem):
        self.title = title
        self.poet = poet
        self.poem = poem

    @classmethod
    def from_json(cls, json_data):
        """
        Factory method to create a Poem object from JSON data.
        """
        try:
            result = json_data["results"]["result"]
            return cls(
                title=result.get("title", "N/A"),
                poet=result.get("poet", "N/A"),
                poem=result.get("poem", "N/A"),
            )
        except (KeyError, TypeError) as e:
            print(f"Error parsing JSON: {e}")
            return None

    def __repr__(self):
        """
        Returns a string representation of the Poem object.
        """
        return (
            f"Poem(title='{self.title}', "
            f"poet='{self.poet}', "
            f"poem='{self.poem}')"
        )

    def to_dict(self):
        """
        Converts the Poem object back to a dictionary.
        """
        return {
            "title": self.title,
            "poet": self.poet,
            "poem": self.poem,
        }
