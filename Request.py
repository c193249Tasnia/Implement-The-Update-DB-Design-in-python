
# 2. Error Handling: Add error handling 
# to both functions to manage exceptions like connection errors or timeouts.
import requests

def get_example():
    
    url = 'https://jsonplaceholder.typicode.com/posts'
    try:
        response = requests.get(url)
        
        response.raise_for_status()  
        print("GET request successful!")
        
        posts = response.json()       
        for i, post in enumerate(posts, start=1):
            print(f"Post {i}:")
            print(post)
            print()  
            
    except requests.RequestException as e:
        print(f"Failed to retrieve data: {e}")

def post_example():
    
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title': 'HEY',
        'body': 'THIS IS MY CODE',
        'userId': 15
    }
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  
        print("POST request successful!")
        print(response.json())
        
    except requests.RequestException as e:
        print(f"Failed to post data: {e}")

def main():
    print("Executing GET example...")
    get_example()
    print("\nExecuting POST example...")
    post_example()

if __name__ == "__main__":
    main()
