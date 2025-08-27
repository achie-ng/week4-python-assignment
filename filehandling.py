def main():
    filename = input("Enter the file name to read:").strip()
    try:
        with open(filename, "r" ,encoding="utf-8")as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist")
        return
    except PermissionError:
        print(f"Error: no permission to read ''{filename}'.")
        return
    except Exception as e:
        print(f"Unexpected read error: {e}")
        return
    choice = input("Modify: upper/lower/reverse?").strip().lower()
    if choice == "upper":
        modified = content.upper()
    elif choice == "lower":
        modified = content.lower()
    elif choice =="reverse":
        modifed = content[::-1]
    else:
        print("Unknown option; leaving content unchanged.")
        modified = content
    outname = f"modified_{filename}"
    try:
        with open(outname,"w", encoding="utf-8")as f:
            f.write(modified)
        print(f"done! Saved to {outname}")
    except Exception as e:
        print("Write error:{e}")
if __name__ == "__main__":
    main()

