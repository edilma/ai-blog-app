# AI Blog App Examples
This directory contains a self-contained, working example of the AI Blog App library. It's the best way to quickly see the framework in action.

## How to Run the Example

1.  **Navigate** to this directory in your terminal.

    ```bash
    cd examples
    ```

2.  **Configure** your API credentials creating a new .env file
    - The example is set up to use one of the popular LLMs configured in main.py. You can easily switch the active model by editing the main.py file.
    - Copy the template from .env.example.
    ```bash
    # On Windows
    copy .env.example .env

    # On macOS or Linux
    cp .env.example .env
    ```
    - **ACTION** Edit the new .env file to add your API keys for the models you want to use.

3. **Create and Activate**  a new virtual enviroment
    ```bash
        python3 -m venv env
    ```
4. **Activate**  the virtual enviroment
    ```bash
        # On Windows
    .\env\Scripts\activate

    # On macOS or Linux
    source env/bin/activate
    ```
5.  **Install** the necessary dependencies for this example.

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run** the main script.

    ```bash
    python main.py
    ```
This will start the multi-agent system, which will generate a blog post based on the topic provided in the example ("How to use AI for business ideas generation").
