import sys

from ft_filter import ft_filter

def main():
  """
  Main function to filter words longer than x characters from a sentence
  """

  try:
    if (
      len(sys.argv) != 3
      or not sys.argv[1]
      or not sys.argv[2].isdigit()
      or int(sys.argv[2]) < 0
    ):
      raise AssertionError("the arguments are bad.")
    
    sentence = sys.argv[1]
    length = int(sys.argv[2])
    words = sentence.split()
    filtered = ft_filter(lambda w: len(w) > length, words)
    print(list(filtered))
  except AssertionError as error:
    print(f"AssertionError: {error}")
  except Exception as error:
    print(f"Unexpected error: {error}")

if __name__ == "__main__":
  main()
