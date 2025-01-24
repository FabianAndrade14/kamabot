# Chatbot "Kamabot"
Based on Tanjiro Kamado's name and the necessity to create an IA assistant to my personal projects, i took the first step to implement a kind bot to answer all the questions make for the users of the application. This bot can be trained in any topic. 
## Funcitonality
To execute this project, you'll need to follow this steps:
1. Configure the virtual environment, using the following command:
```
python -m venv chatbot_env
chatbot_env\Scripts\activate
```
2. Now, in this step, install all the dependencies
```
pip install flask requests tensorflow sklearn nltk python-dotenv
```
Note: for the deprecated packages, like sklearn, try to update the pip, to the 24 version before you go forward in this guide. to replace the sklearn, the updated package is scikit-learn.
```
pip install scikit-learn
```