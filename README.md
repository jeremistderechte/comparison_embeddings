# Description 

This project explores and compares various embedding models.. It was developed as part of the Data Management Fundamentals lecture 🚀.


## Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python**
- **Poetry**

Make sure you have a database (postgresql) running and pgvector installed, for ubuntu/debian systems you can install pgvector with this (postgresql is preinstalled on ubuntu):

   ```bash
   sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

   wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |  sudo apt-key add -

   sudo apt-get update
   sudo apt-get upgrade
   sudo apt install postgresql-16-pgvector
   sudo apt-get install libpq-dev # fuer psycopg2
   ```

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
   If you don't want to use poetry there is also a requirements.txt.

   pgadmin4 will be installed over pip, you need to create folders for that if not already made:

    ```bash
    sudo mkdir /var/lib/pgadmin
    sudo mkdir /var/log/pgadmin
    sudo chown \$USER /var/lib/ pgadmin
    sudo chown \$USER /var/log/ pgadmin
    pgadmin4
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
Once everything is set up, you need to do this steps:

Create your own database, see /notebooks/db.sql for an example. After that you can run the code in:

```bash
/notebooks/embeddings.ipynb 
```

## Dataset
This project uses the [Amazon Reviews Dataset](https://www.kaggle.com/datasets/dongrelaxman/amazon-reviews-dataset), distributed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). Please ensure compliance with its licensing terms if using or modifying this dataset.

