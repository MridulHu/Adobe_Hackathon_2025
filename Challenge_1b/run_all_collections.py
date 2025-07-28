import os
from process_collection import process_collection

def run_all_collections(base_dir="."):
    for name in os.listdir(base_dir):
        collection_path = os.path.join(base_dir, name)
        if (
            os.path.isdir(collection_path)
            and name.startswith("collection_")
        ):
            print(f"\n🔍 Processing: {collection_path}")
            process_collection(collection_path)

if __name__ == "__main__":
    run_all_collections()
