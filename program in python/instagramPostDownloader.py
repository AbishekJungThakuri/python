import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Optionally, login to Instagram (required for private profiles)
# loader.login('your_username', 'your_password')

# Download a single post by URL
def download_post(url):
    try:
        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
        loader.download_post(post, target='insta_downloads')
        print(f"Downloaded post: {url}")
    except Exception as e:
        print(f"Failed to download post: {e}")

# Download all posts from a profile
def download_profile(username):
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        for post in profile.get_posts():
            loader.download_post(post, target=f'insta_downloads/{username}')
            print(f"Downloaded post: {post.url}")
    except Exception as e:
        print(f"Failed to download profile: {e}")

# Example usage
if __name__ == "__main__":
    # Download a specific post by URL
    post_url = "https://www.instagram.com/reel/DEcY1LEyXyA/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=="  # Replace with the actual post URL
    download_post(post_url)

    # Download all posts from a profile
    profile_username = "instagram"  # Replace with the actual username
    download_profile(profile_username)