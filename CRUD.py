class SafetyRecordManager:
    def __init__(self):
        self.safety_records = {}
        self.safety_improvements = {}

    def create_safety_record(self, stadium_id, safety_data):
        if stadium_id not in self.safety_records:
            self.safety_records[stadium_id] = []
        self.safety_records[stadium_id].append(safety_data)
        return f"Safety record for stadium {stadium_id} created successfully!"

    def read_safety_records(self, stadium_id):
        records = self.safety_records.get(stadium_id, [])
        return records if records else f"No safety records found for stadium {stadium_id}."

    def update_safety_record(self, stadium_id, record_id, updated_data):
        record_id -= 1  # Convert to 1-based index
        if stadium_id in self.safety_records:
            records = self.safety_records[stadium_id]
            if 0 <= record_id < len(records):
                records[record_id].update(updated_data)
                return f"Safety record {record_id + 1} updated successfully for stadium {stadium_id}."
            return f"Record {record_id + 1} not found for stadium {stadium_id}."
        return f"Stadium {stadium_id} not found."

    def delete_safety_record(self, stadium_id, record_id):
        record_id -= 1  # Convert to 1-based index
        if stadium_id in self.safety_records:
            records = self.safety_records[stadium_id]
            if 0 <= record_id < len(records):
                del records[record_id]
                return f"Safety record {record_id + 1} deleted successfully for stadium {stadium_id}."
            return f"Record {record_id + 1} not found for stadium {stadium_id}."
        return f"Stadium {stadium_id} not found."

    def conduct_safety_audit(self, stadium_id):
        return {
            'stadium_id': stadium_id,
            'audit_results': 'All systems operational, no immediate concerns.',
            'audit_score': 95
        }

    def manage_safety_improvements(self, improvement_data):
        improvement_id = len(self.safety_improvements) + 1
        improvement_data['improvement_id'] = improvement_id
        self.safety_improvements[improvement_id] = improvement_data
        return f"Safety improvement {improvement_id} added successfully!"

    def get_safety_improvements(self):
        return self.safety_improvements if self.safety_improvements else "No safety improvements found."
