def clean_data(data):
    """Dummy data cleaning function"""
    return data.strip().lower()

if __name__ == "__main__":
    sample = " Hello World "
    print(clean_data(sample))
