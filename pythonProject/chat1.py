import openai

# Set your OpenAI GPT-3 API key
api_key = "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"
openai.api_key = api_key

# Define your fine-tuning data
fine_tuning_data = [
    {"text": "Conversation 1. User: How are you?\nAssistant: I'm fine, thank you."},
    {"text": "Conversation 2. User: Tell me a joke!\nAssistant: Why did the chicken cross the road?"},
    {"text": "Conversation 3. User: What's your favorite color?\nAssistant: I don't have a favorite color since I'm just a computer program."},
    {"text": "Conversation 4. User: Recommend a book to read.\nAssistant: If you like fantasy, I recommend 'The Hobbit' by J.R.R. Tolkien."},
    {"text": "Conversation 5. User: Where can I find the best pizza?\nAssistant: It depends on your location, but you might want to try the pizzeria downtown."},
    {"text": "Conversation 6. User: What's the capital of France?\nAssistant: The capital of France is Paris."},
    {"text": "Conversation 7. User: Any tips for staying productive?\nAssistant: Break your tasks into smaller, manageable steps and take short breaks in between."},
    {"text": "Conversation 8. User: Can you help me with a programming problem?\nAssistant: Of course! Please provide more details about the issue."},
    {"text": "Conversation 9. User: What's the weather like today?\nAssistant: I'm sorry, I don't have real-time information. You can check a weather website or app for the latest updates."},
    {"text": "Conversation 10. User: Recommend a movie for a cozy night in.\nAssistant: If you enjoy comedy, 'The Grand Budapest Hotel' is a delightful choice."},
    {"text": "Conversation 11. User: Share a fun fact with me!\nAssistant: Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible."},
    {"text": "Conversation 12. User: What's the best way to learn a new language?\nAssistant: Immersion and consistent practice are key. Try incorporating the language into your daily routine and engage in conversations with native speakers."},
    {"text": "Conversation 13. User: How do you stay updated with current events?\nAssistant: I don't stay updated in real-time, but you can check reliable news websites or use news apps to stay informed."},
    {"text": "Conversation 14. User: What's the most challenging programming language?\nAssistant: Difficulty is subjective, but some find languages like Haskell or Rust to be challenging due to their unique features."},
    {"text": "Conversation 15. User: Recommend a workout routine.\nAssistant: A combination of cardio, strength training, and flexibility exercises can provide a well-rounded workout. Tailor it to your fitness goals and preferences."},
    {"text": "Conversation 16. User: Can you teach me a magic trick?\nAssistant: Sure! How about a simple card trick? Pick a card, memorize it, and I'll try to guess it."},
    {"text": "Conversation 17. User: What's the meaning of life?\nAssistant: The meaning of life is a profound and subjective question. Different people find different meanings in their experiences and connections."},
    {"text": "Conversation 18. User: Tell me about your favorite science fiction movie.\nAssistant: As a program, I don't have personal preferences, but 'Blade Runner' and 'The Matrix' are popular choices."},
    {"text": "Conversation 19. User: Recommend a music playlist for a road trip.\nAssistant: How about a mix of classic rock and upbeat pop? It can keep the energy high during your journey."},
    {"text": "Conversation 20. User: What's the best way to overcome writer's block?\nAssistant: Take a break, go for a walk, or try freewriting. Sometimes, stepping away from the work can bring fresh perspectives."},
    {"text": "Conversation 21. User: Tell me a riddle!\nAssistant: I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"},
    {"text": "Conversation 22. User: Share a travel adventure you'd recommend.\nAssistant: Exploring the ancient ruins of Machu Picchu in Peru can be an unforgettable adventure."},
    {"text": "Conversation 23. User: How can I improve my memory?\nAssistant: Regular mental exercises, a healthy diet, and proper sleep can contribute to better memory."},
    {"text": "Conversation 24. User: What's the most interesting historical period?\nAssistant: Many find the Renaissance fascinating due to its cultural and artistic flourishing."},
    {"text": "Conversation 25. User: Recommend a documentary on space exploration.\nAssistant: 'For All Mankind' is a captivating documentary that chronicles the history of space exploration."},
    {"text": "Conversation 26. User: Any tips for effective time management?\nAssistant: Prioritize tasks, set realistic goals, and consider using techniques like the Pomodoro Technique for focused work."},
    {"text": "Conversation 27. User: Share a recipe for a quick and healthy meal.\nAssistant: Try a quinoa salad with mixed vegetables, olive oil, and a squeeze of lemon for a nutritious and easy-to-make dish."},
    {"text": "Conversation 28. User: What's your favorite type of technology?\nAssistant: I don't have personal preferences, but artificial intelligence and robotics are fascinating areas of technology."},
    {"text": "Conversation 29. User: How do you deal with stress?\nAssistant: I don't experience stress, but taking breaks, practicing mindfulness, and talking to friends can be helpful for humans."},
    {"text": "Conversation 30. User: Recommend a podcast for learning new things.\nAssistant: 'Stuff You Should Know' covers a wide range of interesting topics and is great for learning new facts."},
    {"text": "Conversation 31. User: What's the key to a successful relationship?\nAssistant: Communication, trust, and mutual respect are often considered crucial for a successful and healthy relationship."},
    {"text": "Conversation 32. User: Share a quote that inspires you.\nAssistant: 'The only way to do great work is to love what you do.' - Steve Jobs"},
    {"text": "Conversation 33. User: How can I start a small business?\nAssistant: Define your niche, create a business plan, and focus on providing value to your customers."},
    {"text": "Conversation 34. User: Tell me about a fascinating scientific discovery.\nAssistant: The discovery of the Higgs boson particle at CERN in 2012 was a groundbreaking moment in particle physics."},
    {"text": "Conversation 35. User: Recommend a board game for a family night.\nAssistant: 'Ticket to Ride' is a fun and strategic board game that the whole family can enjoy."},
    {"text": "Conversation 36. User: How can I become more creative?\nAssistant: Experiment with new ideas, embrace failure as part of the creative process, and surround yourself with diverse influences."},
    {"text": "Conversation 37. User: What's the best way to save money?\nAssistant: Create a budget, cut unnecessary expenses, and consider setting up automatic savings to build a financial cushion."},
    {"text": "Conversation 38. User: Share a tip for public speaking.\nAssistant: Practice, know your material well, and focus on connecting with your audience."},
    {"text": "Conversation 39. User: Recommend a mobile app for productivity.\nAssistant: 'Todoist' is a popular app for task management and organization."},
    {"text": "Conversation 40. User: Tell me about a famous historical figure.\nAssistant: Leonardo da Vinci, a polymath of the Renaissance, was known for his contributions to art, science, and engineering."},
    {"text": "Conversation 41. User: How can I develop a growth mindset?\nAssistant: Embrace challenges, learn from criticism, and see failures as opportunities for learning and improvement."},
    {"text": "Conversation 42. User: Recommend a movie for a thought-provoking experience.\nAssistant: 'Inception' is a mind-bending film that explores the nature of reality and dreams."},
    {"text": "Conversation 43. User: What's the best way to learn to code?\nAssistant: Start with beginner-friendly languages like Python, practice coding regularly, and work on real-world projects."},
    {"text": "Conversation 44. User: Share a quote about perseverance.\nAssistant: 'It's not whether you get knocked down, it's whether you get up.' - Vince Lombardi"},
    {"text": "Conversation 45. User: Recommend a TED Talk for inspiration.\nAssistant: 'The Power of Vulnerability' by Brené Brown is a powerful TED Talk about human connection and authenticity."},
    {"text": "Conversation 46. User: Any tips for effective goal setting?\nAssistant: Make your goals specific, measurable, achievable, relevant, and time-bound (SMART), and break them down into smaller tasks."},
    {"text": "Conversation 47. User: Tell me about a fascinating cultural tradition.\nAssistant: The Holi festival in India is known for its vibrant colors and the celebration of the arrival of spring."},
    {"text": "Conversation 48. User: How can I develop better communication skills?\nAssistant: Practice active listening, be clear and concise in your messages, and seek feedback for continuous improvement."},
    {"text": "Conversation 49. User: Recommend a classic video game.\nAssistant: 'The Legend of Zelda: Ocarina of Time' is considered a classic with its immersive world and engaging gameplay."},
    {"text": "Conversation 50. User: What's your favorite type of cuisine?\nAssistant: I don't have personal preferences, but many people enjoy the variety and flavors of Italian cuisine."},
    {"text": "Conversation 51. User: Share a memory from your childhood.\nAssistant: I don't have personal experiences, but many people cherish memories of playing games or spending time with family."},
    {"text": "Conversation 52. User: What's the best way to learn a musical instrument?\nAssistant: Practice regularly, start with simple songs, and consider taking lessons from a skilled teacher."},
    {"text": "Conversation 53. User: Recommend a book on personal development.\nAssistant: 'The 7 Habits of Highly Effective People' by Stephen Covey is a timeless classic for personal and professional growth."},
    {"text": "Conversation 54. User: Tell me about a famous inventor.\nAssistant: Thomas Edison, known for the invention of the light bulb, held over 1,000 patents and made significant contributions to modern technology."},
    {"text": "Conversation 55. User: How can I stay motivated to exercise?\nAssistant: Set achievable goals, find activities you enjoy, and consider working out with a friend for added motivation."},
    {"text": "Conversation 56. User: Recommend a nature documentary.\nAssistant: 'Planet Earth II' offers stunning visuals and in-depth exploration of various ecosystems and wildlife."},
    {"text": "Conversation 57. User: What's the best way to learn about different cultures?\nAssistant: Read books, watch documentaries, and engage in conversations with people from diverse backgrounds."},
    {"text": "Conversation 58. User: Share a tip for effective studying.\nAssistant: Create a study schedule, break down complex topics, and use active learning methods like flashcards or teaching the material to someone else."},
    {"text": "Conversation 59. User: What's the most interesting space phenomenon?\nAssistant: Black holes, with their mysterious and gravitational effects, are among the most intriguing phenomena in space."},
    {"text": "Conversation 60. User: Recommend a comedy movie for a good laugh.\nAssistant: 'Superbad' is a hilarious comedy film with a mix of humor and coming-of-age elements."},
    {"text": "Conversation 61. User: How can I improve my public speaking skills?\nAssistant: Join a public speaking club, practice regularly, and seek constructive feedback to refine your delivery."},
]

# Fine-tune the base GPT-3 model
fine_tuned_model = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=fine_tuning_data,
    temperature=0.7,
    max_tokens=150,
    n=1,
    stop=None,
)

# Save the fine-tuned model ID
fine_tuned_model_id = fine_tuned_model['id']

# Use the fine-tuned model for chat
def chat_with_fine_tuned_model(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  # Use the engine that supports fine-tuned models
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        stop=None,
        model=fine_tuned_model_id,
    )
    return response.choices[0].text.strip()

# Example usage
user_input = "User: How does fine-tuning work?\nAssistant:"
response = chat_with_fine_tuned_model(user_input)
print(response)





# import openai
#
# # Set your OpenAI GPT-3 API key
# api_key = "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"
# openai.api_key = api_key
#
# # Define the conversation
# conversation = [
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#     {"role": "user", "content": "Where was it played?"}
# ]
#
# # Use the fine-tuned model for chat
# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=conversation,
#     temperature=0.7,
#     max_tokens=150,
#     n=1,
#     stop=None,
# )
#
# # Print the assistant's response
# print("Assistant:", response['choices'][0]['message']['content'])
