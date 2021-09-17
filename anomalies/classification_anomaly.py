class ClassificationAnomaly(Exception):
    def __init__(self):
        self.base_message = "It was not possible to complete the solution of the differential equation because it could not be detected by our server or the backup system as one of the supported types."
        self.final_solve = []
        super().__init__(self.base_message)

    def set_final_solve(self, solve):
        self.final_solve = solve

    def to_json(self):
        return {"message": self.base_message, "solution": self.final_solve}