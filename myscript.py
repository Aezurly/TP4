import os

BAD_HASH = "c1a4be04b972b6c17db242fc37752ad517c29402"
GOOD_HASH = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

def main():
    os.system(f"git bisect start {BAD_HASH} {GOOD_HASH}")
    
    os.system("git bisect run python manage.py test")
    os.system("git bisect reset")
    
    exit()

if __name__ == "__main__":
    main()