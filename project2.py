class Critic:
    def __init__(self, name):
        self.name = name

class Review:
    def __init__(self, review_id, critic, content):
        self.review_id = review_id
        self.critic = critic
        self.content = content

class Comment:
    def __init__(self, commenter, text):
        self.commenter = commenter
        self.text = text

class Discussion:
    def __init__(self, discussion_id, topic):
        self.discussion_id = discussion_id
        self.topic = topic
        self.comments = []

    def add_comment(self, commenter, text):
        self.comments.append(Comment(commenter, text))

    def delete_comment(self, comment_index):
        if 0 <= comment_index:
            del self.comments[comment_index]
            return True
        else:
            return False

class FilmCriticPlatform:
    def is_manager(self):
        return self.logged_in_user == self.manager_username
    def __init__(self):
        self.reviews = {}
        self.discussions = {}
        self.critics = []
        self.logged_in_user = None
        self.users = {"goa": "p2","vamshi":"p3","prajwal":"p4"} 
        self.manager_username = "surya"
        self.manager_password = "p1"
    
    def view_all_comments(self):
        print("All User Comments:") 
        for discussion_id, discussion in self.discussions.items():
            print(f"Discussion ID: {discussion_id}")
            print("Comments:")
            for index, comment in enumerate(discussion.comments):
                print(f"  {index + 1}. Commenter: {comment.commenter}, Text: {comment.text}")
            print()
    
    def user_login(self, username, password):
        if username in self.users and self.users[username] == password:
            self.logged_in_user = username
            print("User login successful.")
        else:
            print("Invalid username or password.")
        pass

    def manager_login(self, username, password):
        if username == self.manager_username and password == self.manager_password:
            self.logged_in_user = username
            print("Manager login successful.")
        else:
            print("Invalid username or password.")
        pass

    def publish_film_reviews(self):
        if self.logged_in_user is None:
            print("Please login before publishing a review.")
            return

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
        topic1=input("On Movie:")
        content = input("Content: ")
        if self.create_review(review_id, critic_name, content):
            print("Review published successfully!")
            self.facilitate_critic_discussions()
        else:
            print("Review ID already exists. Please choose a different ID.")

    def facilitate_critic_discussions(self):
        print("Enter details for the discussion:")
        discussion_id = input("Discussion ID: ")
        topic = input("Topic: ")
        self.discussions[discussion_id] = Discussion(discussion_id, topic)
        print("Discussion created successfully!")

    def add_comment_to_discussion(self, discussion_id, commenter, text):
        if discussion_id in self.discussions:
            self.discussions[discussion_id].add_comment(commenter, text)
            print("Comment added successfully!")
        else:
            print("Discussion ID does not exist.")

    def delete_comment_from_discussion(self, discussion_id, comment_index):
        if discussion_id in self.discussions:
            if self.discussions[discussion_id].delete_comment(comment_index):
                print("Comment deleted successfully!")
            else:
                print("Invalid comment index.")
        else:
            print("Discussion ID does not exist.")

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

    def view_all_reviews(self):
        print("All Published Reviews:")
        for review_id, review in self.reviews.items():
            print(f"Review ID: {review_id}, Critic: {review.critic}, Content: {review.content}")


def main():
    platform = FilmCriticPlatform()

    while True:
        if platform.logged_in_user:
            if platform.is_manager():
             if platform.is_manager():
                print("\nManager Menu:")
                print("1. Publish Critic Review")
                print("2. Facilitate Critic Discussions")
                print("3. View All Film Discussions")
                print("4. Add Comment to Discussion")
                print("5. Delete Comment from Discussion")
                print("6. Add Critic")
                print("7. View All Film Critics")
                print("8. View All Published Reviews")
                print("9. View All User Comments")
                print("10. Logout")
                choice = input("Enter your choice (1-10): ")
                
                if choice == '1':
                    platform.publish_film_reviews()
                elif choice == '2':
                    platform.facilitate_critic_discussions()
                elif choice == '3':
                    platform.view_all_discussions()
                elif choice == '4':
                    discussion_id = input("Enter Discussion ID: ")
                    commenter = input("Enter Your Name: ")
                    text = input("Enter Your Comment: ")
                    platform.add_comment_to_discussion(discussion_id, commenter, text)
                elif choice == '5':
                    discussion_id = input("Enter Discussion ID: ")
                    comment_index = int(input("Enter Index of Comment to Delete: "))
                    platform.delete_comment_from_discussion(discussion_id, comment_index)
                elif choice == '6':
                    critic_name = input("Enter critic name: ")
                    platform.add_critic(critic_name)
                elif choice == '7':
                    platform.view_all_critics()
                elif choice == '8':
                    platform.view_all_reviews()
                elif choice == '9':
                    platform.view_all_comments()
                elif choice == '10':
                    platform.logged_in_user = None
                    print("Logged out successfully.")
                else:
                    print("Invalid choice. Please enter a valid option.")

            else:
                print("\nUser Menu:")
                print("1. View All Film Discussions")
                print("2. Add Comment to Discussion")
                print("3. Delete Comment from Discussion")
                print("4. View All Published Reviews")
                print("5. Logout")
                choice = input("Enter your choice (1-5): ")
                
                if choice == '1':
                    platform.view_all_discussions()
                elif choice == '2':
                    discussion_id = input("Enter Discussion ID: ")
                    commenter = input("Enter Your Name: ")
                    text = input("Enter Your Comment: ")
                    platform.add_comment_to_discussion(discussion_id, commenter, text)
                elif choice == '3':
                    discussion_id = input("Enter Discussion ID: ")
                    comment_index = int(input("Enter Index of Comment to Delete: "))
                    platform.delete_comment_from_discussion(discussion_id, comment_index)
                elif choice == '4':
                    platform.view_all_reviews()
                elif choice == '5':
                    platform.logged_in_user = None
                    print("Logged out successfully.")
                else:
                    print("Invalid choice. Please enter a valid option.")
        else:
            print("\nFilm Critic Collaboration Platform Menu:")
            print("1. User Login")
            print("2. Manager Login")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ")
            
            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                platform.user_login(username, password)
            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                platform.manager_login(username, password)
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()