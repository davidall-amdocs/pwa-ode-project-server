class ClassificationAnomaly(Exception):
    def __init__(self):
        self.base_message = "It was not possible to complete the solution of the differential equation because it could not be detected by our server as one of the supported types."
        super().__init__(self.base_message)

    def to_json(self):
        return {"message": self.base_message}