from send_request import data_from_response


class ProcessActivities:
    def __init__(self, response_data):
        self.response_data = response_data
        self.pricey_activities = self.save_activities_with_price()
        self.pricey_activities.sort(key=self.sortkey)

    def save_activities_with_price(self) -> list:
        pricey_activities = [activity for activity in self.response_data if activity["price"] > 0]
        return pricey_activities

    def sortkey(self, element):
        return element["accessibility"]

if __name__ == "__main__":
    process_instance = ProcessActivities(data_from_response)
    print(process_instance.pricey_activities)
