class Stats:
  """ Class for calculation of statistics operations"""

  @staticmethod
  def ft_sqrt(x: float, epsilon: float = 1e-10) -> float | None:
    """Approximate the square root of x using Newton-Raphson method."""
    if x < 0:
        return None  # Pas de racine carrée réelle pour les négatifs
    if x == 0:
        return 0.0

    guess = x / 2.0
    while abs(guess * guess - x) > epsilon:
        guess = (guess + x / guess) / 2.0
    return guess

  @staticmethod
  def calc_mean(values: list[float]) -> float | None:
    """Compute and return the mean of a list of floats."""
    if len(values) == 0:
      return None
    return sum(values) / len(values)

  @staticmethod
  def calc_median(values: list[float]) -> float | None:
    """ Compute and return the median of a list of floats."""
    n = len(values)
    if n == 0:
      return None

    sorted_values = sorted(values)
    mid = n  // 2
    if n % 2 == 0:
      # if n is pair, mean of both middle values
      return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
      # if not, middle value
      return sorted_values[mid]

  @staticmethod
  def calc_quartiles(values: list[float]) -> list[float] | None:
    """ Compute and return the 25% and 75% quartiles of a list of floats."""
    n = len(values)
    if n == 0:
        return None

    sorted_values = sorted(values)

    def interpolate(p: float) -> float:
        pos = p * (n - 1)
        lower = int(pos)
        upper = min(lower + 1, n - 1)
        weight = pos - lower
        return sorted_values[lower] * (1 - weight) + sorted_values[upper] * weight

    q25 = interpolate(0.25)
    q75 = interpolate(0.75)

    return [q25, q75]

  @staticmethod
  def calc_var(values: list[float]) -> float | None:
    """ Compute and return the variance of a list of float."""
    n = len(values)
    if n == 0:
      return None
    mean = Stats.calc_mean(values)
    return sum((x - mean) ** 2 for x in values) / n
  
  @staticmethod
  def calc_deviat(values: list[float]) -> float | None:
    """ Compute and return the standard deviation of a list of float."""
    variance = Stats.calc_var(values)
    if variance is None:
      return None
    return Stats.ft_sqrt(variance)

def ft_statistics(*args: any, **kwargs: any) -> None:
  """ Compute and return the calculations needed by kwargs if exists."""
  # Filtrer les floats dans args
  values = [float(x) for x in args if isinstance(x, (int, float))]

  # Vérifications des contenus
  if len(values) == 0:
    print("Error: Na valid values in Args!")
    return
  if all(x == 0.0 for x in values):
    print("Error: This a list of 0!")
    return
  if (len(values) < 2):
    print("Error: too few values for some calculations!")
    return

  # Calculs autorisés
  valid_keys = {"mean", "median", "quartile", "std", "var"}

  # Extraire les opérations demandées à partir des valeurs des kwargs
  requested_ops = [op for op in kwargs.values() if op in valid_keys]

  for key in requested_ops:
    match key:
      case "mean":
        print("Mean: ", Stats.calc_mean(values))
      case "median":
        print("Median: ", Stats.calc_median(values))
      case "quartile":
        print("Quartile: ", Stats.calc_quartiles(values))
      case "std":
        print("Standard deviation: ", Stats.calc_deviat(values))
      case "var":
        print("Variance: ", Stats.calc_var(values))
