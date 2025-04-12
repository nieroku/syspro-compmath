#include <cmath>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numbers>
#include <string>

static const int MAX_ITERATIONS = 100000;

using std::numbers::pi;
static const double pi2 = pi / 2;
static const double inf = std::numeric_limits<double>::infinity();

double cot(double x) { return std::cos(x) / std::sin(x); }

double f(double x) { return std::tan(x) - x; }
double df(double x) { return std::tan(x) * std::tan(x); }

double bisection_(double a, double b, double precision) {
  double c = (a + b) / 2;
  if (std::abs(a - b) < 2 * precision)
    return c;
  if (f(c) <= 0)
    a = c;
  else
    b = c;
  __attribute__((musttail)) return bisection_(a, b, precision);
}

double bisection(int k, double precision) {
  return bisection_(pi * k - pi2, pi * k + pi2, precision);
}

double fixed_point_iterations(int k, double precision) {
  double x = k * pi;
  double x1;
  while (std::fabs((x1 = std::atan(x) + k * pi) - x) >= precision)
    x = x1;
  return x;
}

double newton_method(int k, double precision) {
  double x = k * pi + (k >= 0 ? 1 : -1) * (pi2 - precision);
  do {
    x -= f(x) / df(x);
  } while (std::abs(std::tan(x) - x) >= precision);
  return x;
}

double secant_method_step(double& x, double& x1) {
  double x2 = x1 - (f(x1) * (x1 - x) / (f(x1) - f(x)));
  x = x1;
  x1 = x2;
  return std::abs(x1 - x);
}

double secant_method(int k, double precision) {
  double x = k * pi + (k >= 0 ? 1 : -1) * (pi2 - precision);
  double x1 = x - (k >= 0 ? 1 : -1) * (precision);

  for (int i = 0; i < 5; i++)
    secant_method_step(x, x1);

  double delta;
  do {
    delta = secant_method_step(x, x1);
  } while (delta > precision);

  double delta0;
  do {
    delta0 = delta;
    delta = secant_method_step(x, x1);
  } while (delta < delta0);
  return x;
}

int main() {
  std::string line;
  int k;
  double precision;

  std::cout << std::setprecision(9) << std::fixed;
  std::cout << "tg x = x (x in [k * pi - pi/2, k * pi + pi/2])" << '\n';
  std::cout << "Enter k (default 1): " << std::flush;
  std::getline(std::cin, line);
  k = line.empty() ? 1 : std::stoi(line);
  std::cout << "Enter precision (default 0.00001): " << std::flush;
  std::getline(std::cin, line);
  precision = line.empty() ? 0.00001 : std::stod(line);
  std::cout << '\n';

  using Method = std::function<double(int, double)>;
  auto methods = std::to_array<std::pair<const char*, Method>>({
      std::make_pair("bisection", bisection),
      std::make_pair("fixed-point iterations", fixed_point_iterations),
      std::make_pair("newton method", newton_method),
      std::make_pair("secant method", secant_method),
  });

  for (const auto [name, method] : methods) {
    std::cout << name << ":" << '\n';
    std::cout << "x = " << method(k, precision) << '\n';
    std::cout << '\n';
  }
}
