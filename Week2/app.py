import asyncio
import aiohttp

# Async function
async def fetch_post(session, post_id):

    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    async with session.get(url) as response:

        data = await response.json()

        print(f"Fetched post {post_id}")

        return data


# Main async function
async def main():

    async with aiohttp.ClientSession() as session:

        tasks = []

        # Create 10 tasks
        for i in range(1, 11):

            task = fetch_post(session, i)

            tasks.append(task)

        # Run all tasks concurrently
        results = await asyncio.gather(*tasks)

        print("\nAll API calls completed!\n")

        # Print titles
        for result in results:

            print(result["title"])


# Start program
asyncio.run(main())