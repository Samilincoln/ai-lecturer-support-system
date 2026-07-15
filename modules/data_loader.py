#======================Load excel file as df===============

import pandas as pd

import pandas as pd

def load_excel_data(file_path):
    """Load data from CSV or Excel file based on extension or content type."""
    try:
        # Check if it's a Streamlit UploadedFile object
        if hasattr(file_path, 'name'):
            filename = file_path.name
        else:
            filename = file_path  # Assume it's a string path

        if filename.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif filename.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file_path, engine="openpyxl")
        else:
            raise ValueError("Unsupported file format. Use .csv, .xlsx, or .xls")

        return df

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except pd.errors.ParserError:
        raise ValueError("Failed to parse file. Please check the file content and format.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while loading the file: {str(e)}")




# def load_excel_data(file_path):
#     """Load data from CSV or Excel file based on extension or content type"""
#     # Check if it's a Streamlit UploadedFile object
#     if hasattr(file_path, 'name'):
#         # Get the filename from the UploadedFile object
#         filename = file_path.name
        
#         if filename.endswith('.csv'):
#             df = pd.read_csv(file_path)
#             return df
#         elif filename.endswith(('.xlsx', '.xls')):
#             df = pd.read_excel(file_path)
#             return df
#         else:
#             raise ValueError("Unsupported file format. Use .csv, .xlsx, or .xls")
#     else:
#         # Handle regular file paths (strings)
#         if file_path.endswith('.csv'):
#             df = pd.read_csv(file_path)
#             return df
#         elif file_path.endswith(('.xlsx', '.xls')):
#             df = pd.read_excel(file_path)
#             return df
#         else:
#             raise ValueError("Unsupported file format. Use .csv, .xlsx, or .xls")