class Critic:
    def __init__(self, name):
        self.name = name

class Review:
    def __init__(self, review_id, critic, content):
        self.review_id = review_id
        self.critic = critic
        self.content = content

class Discussion:
    def __init__(self, discussion_id, topic):
        self.discussion_id = discussion_id
        self.topic = topic

class FilmCriticPlatform:
    def __init__(self):
        self.reviews = {}
        self.discussions = {}
        self.critics = []

    def create_review(self, review_id, critic, content):
        if review_id not in self.reviews:
            self.reviews[review_id] = Review(review_id, critic, content)
            return True
        else:
            return False

    def read_review(self, review_id):
        if review_id in self.reviews:
            return self.reviews[review_id]
        else:
            return None

    def update_review(self, review_id, new_content):
        if review_id in self.reviews:
            self.reviews[review_id].content = new_content
            return True
        else:
            return False

    def delete_review(self, review_id):
        if review_id in self.reviews:
            del self.reviews[review_id]
            return True
        else:
            return False

    def publish_film_reviews(self):
        print("Enter details for the review:")
        review_id = input("Review ID: ")
        critic_name = input("Critic Name: ")
        content = input("Content: ")
        if self.create_review(review_id, critic_name, content):
            print("Review published successfully!")
        else:
            print("Review ID already exists. Please choose a different ID.")

    def facilitate_critic_discussions(self):
        print("Enter details for the discussion:")
        discussion_id = input("Discussion ID: ")
        topic = input("Topic: ")
        self.discussions[discussion_id] = Discussion(discussion_id, topic)
        print("Discussion created successfully!")

    def view_all_discussions(self):
        print("All Film Discussions:")
        for discussion_id, discussion in self.discussions.items():
            print(f"Discussion ID: {discussion_id}, Topic: {discussion.topic}")

    def add_critic(self, critic_name):
        self.critics.append(Critic(critic_name))
        print("Critic added successfully!")

    def view_all_critics(self):
        print("All Film Critics:")
        for critic in self.critics:
            print(f"Critic Name: {critic.name}")

def main():
    platform = FilmCriticPlatform()

    while True:
        print("\nFilm Critic Collaboration Platform Menu:")
        print("1. Publish Film Reviews")
        print("2. Facilitate Critic Discussions")
        print("3. View All Film Discussions")
        print("4. Add Critic")
        print("5. View All Film Critics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            platform.publish_film_reviews()
        elif choice == '2':
            platform.facilitate_critic_discussions()
        elif choice == '3':
            platform.view_all_discussions()
        elif choice == '4':
            critic_name = input("Enter critic name: ")
            platform.add_critic(critic_name)
        elif choice == '5':
            platform.view_all_critics()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
