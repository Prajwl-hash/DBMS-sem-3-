from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://prajwlram:123654@cluster1.nzfji.mongodb.net/", tlsAllowInvalidCertificates=True)


print(client)
db = client["youtube"]
video_collection = db["manager"]

# CRUD functions
def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def update_video(video_id, new_name, new_time):
    try:
        result = video_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}})
        if result.matched_count:
            print("Video updated successfully.")
        else:
            print("Video not found.")
    except Exception as e:
        print(f"Error updating video: {e}")

def delete_video(video_id):
    try:
        result = video_collection.delete_one({"_id": ObjectId(video_id)})
        if result.deleted_count:
            print("Video deleted successfully.")
        else:
            print("Video not found.")
    except Exception as e:
        print(f"Error deleting video: {e}")

# Main loop
def main():
    while True:
        print("\nYouTube Manager App")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)  # Fix: Only pass `video_id`
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
