class CompletenessAnomaly(Exception):
    def __init__(self, partial_solution):
        self.base_message = "It was not possible to complete the solution of the differential equation. The server managed to perform these steps: "
        super().__init__(self.base_message)
        self.partial_solution = partial_solution

    def to_json(self):
        return {"partial": self.partial_solution, "message": self.base_message, "kind": self.kind}