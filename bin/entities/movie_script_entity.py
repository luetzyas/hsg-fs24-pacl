class MovieScript:
    def __init__(self, title, subtitle, writer, link):
        self.title = title
        self.subtitle = subtitle
        self.writer = writer
        self.link = link

    @classmethod
    def from_json(cls, json_data):
        """
        Factory method to create a MovieScript object from JSON data.
        """
        try:
            result = json_data["results"]["result"]
            return cls(
                title=result.get("title", "N/A"),
                subtitle=result.get("subtitle", "N/A"),
                writer=result.get("writer", "N/A"),
                link=result.get("link", "N/A")
            )
        except (KeyError, TypeError) as e:
            print(f"Error parsing JSON: {e}")
            return None

    def __repr__(self):
        """
        Returns a string representation of the MovieScript object.
        """
        return (
            f"MovieScript(title='{self.title}', "
            f"subtitle='{self.subtitle}', "
            f"writer='{self.writer}', "
            f"link='{self.link}')"
        )

    def to_dict(self):
        """
        Converts the MovieScript object back to a dictionary.
        """
        return {
            "title": self.title,
            "subtitle": self.subtitle,
            "writer": self.writer,
            "link": self.link
        }
