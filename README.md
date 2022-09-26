# sample-slack-function
This is a python project that shows the most basic functionalities of slack functions

## How to
In order to run this application locally you will need to have [python](https://www.python.org/) and the [SlackCLI](https://api.slack.com/future/tools/cli) installed on your machine

1. Install the dependencies 
   ```bash
   pip install -r requirements.txt
   ```
2. Login to your slack workspace
   ```bash
   slack login
   ```
3. Create the trigger for the function
   ```bash
   slack trigger create --trigger-def manifest/triggers/sample_trigger.json
   ```
4. Start your application
   ```
   slack run
   ```
5. Use the trigger url in your workspace
