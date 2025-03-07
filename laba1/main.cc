#include <cmath>
#include <concepts>
#include <iostream>
#include <typeinfo>

template <std::floating_point T> void run() {
  std::cout << "Working with " << typeid(T).name() << '\n';
  for (int i = 0; i < 80; i++)
    std::cout << '=';
  std::cout << std::hexfloat;

  T one = 1;
  T eps = 1;
  unsigned mantissa_digits = 0;
  while (one + (eps / 2) != one) {
    mantissa_digits += 1;
    eps /= 2;
  }

  T sample = one;
  int min_exp = 0;
  while (std::isnormal(sample / 2)) {
    min_exp--;
    sample /= 2;
  }

  sample = one;
  int max_exp = 0;
  while (!std::isinf(sample * 2)) {
    max_exp++;
    sample *= 2;
  }

  std::cout << "machine eps: " << eps << '\n';
  std::cout << "mantissa has " << mantissa_digits << " digits\n";
  std::cout << "min exp: " << min_exp << '\n';
  std::cout << "max exp: " << max_exp << '\n';

  std::cout << '\n';

  T eps2 = eps / 2;
  if (one == (one + eps2))
    std::cout << one << " == " << (one + eps2) << '\n';
  if (one + eps2 < one + eps)
    std::cout << one + eps2 << " < " << one + eps << '\n';
  if (one + eps < one + eps + eps2)
    std::cout << one + eps << " < " << one + eps + eps2 << '\n';

  std::cout << std::endl;
}

int main() {
  run<float>();
  run<double>();
}
