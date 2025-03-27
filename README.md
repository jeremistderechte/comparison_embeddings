# Description 

This project explores and compares various embedding models.. It was developed as part of the Data Management Fundamentals lecture 🚀.


## Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python**
- **Poetry**

### Step-by-Step Setup

1. **Clone the Repository**  
   Start by cloning the repository to your local machine:

   ```bash
   git clone https://github.com/jeremistderechte/comparison_embeddings.git

   cd comparison_embeddings
   ```

2. **Install Dependencies**  
   Use Poetry to install all required dependencies:

   ```bash
   poetry install
   ```

3. **Activate the Virtual Environment**  
   Enter the virtual environment created by Poetry:

   ```bash
   poetry env activate # returns command to enter env

   poetry shell # if poetry-plugin-shell installed
   ```

4. **Create a `.secrets.toml` File**  
   For secure configuration, create a `.secrets.toml` file in the root directory with the following content:

   ```toml
   db_name = "mydatabase"
   user_name = "myuser"
   password = "mypassword"
   host_ip = "localhost"
   host_port = "5432"
   ```
## Usage

Once everything is set up, you can run the project in the following file:

```bash
/notebooks/embeddings.ipynb 
```

## Dataset
This project uses the [Amazon Reviews Dataset](https://www.kaggle.com/datasets/dongrelaxman/amazon-reviews-dataset), distributed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). Please ensure compliance with its licensing terms if using or modifying this dataset.

