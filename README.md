$$
\renewcommand{\Re}[1]{\,\text{Re}\big[#1\big]}
\renewcommand{\Im}[1]{\,\text{Im}\big[#1\big]}
\newcommand{\Var}[1]{\text{Var}\big(#1\big)}
\newcommand{\Cov}[2]{\text{Cov}\big(#1,#2\big)}
$$

## Fourier

$$
R_n = \sum_{j=1}^{N_b} X_j \, e^{inwt_j}
$$

where $N_b$ is the number of bins.

## Phasor

$$
r_n = \frac{R_n}{R_0}
$$

where

$$
\begin{cases}
\Re{r_n} = \frac{\Re{R_n}}{R_0}
\\[1.5em]
\Im{r_n} = \frac{\Im{R_n}}{R_0}
\end{cases}
$$

since
$$
X_i \in \mathbb{R} \;\; \forall i
\Longrightarrow
R_0 \in \mathbb{R}
$$


## Error propagation

$$
\text{Cov}(r_n) =
\begin{pmatrix}
\Var{\Re{r_n}} & \Cov{\Re{r_n}}{\Im{r_n}}
\\
\\
\Cov{\Re{r_n}}{\Im{r_n}} & \Var{\Im{r_n}}
\end{pmatrix}
$$

### Real part

$$
\begin{align*}
\Var{\Re{r_n}} &=

\\ \text{asuming independence}

&= \sum_j \left(\frac{\partial \Re{r_n}}{\partial X_j} \; \sigma_j \right)^2

\\ \text{chain rule}

&= \sum_j \left(
\left[
\frac{\partial \Re{r_n}}{\partial \Re{R_n}} \frac{\partial \Re{R_n}}{\partial X_j}
+
\frac{\partial \Re{r_n}}{\partial R_0} \frac{\partial R_0}{\partial X_j}
\right]
\; \sigma_j \right)^2

\\ \text{replace derivatives}

&= \sum_j \left(
\left[
\frac{1}{R_0} \cdot \Re{e^{inwt_j}}
-
\frac{\Re{R_n}}{R_0^2} \cdot 1
\right]
\; \sigma_j \right)^2

\\ \text{replace with phasor}

&= \sum_j \left(
\left[
\frac{1}{R_0} \cdot \Re{e^{inwt_j}}
-
\frac{\Re{r_n}}{R_0} \cdot 1
\right]
\; \sigma_j \right)^2

\\ \text{factor out}

&= \frac{1}{R_0^2} \sum_j
\Big( \Re{e^{inwt_j}} - \Re{r_n} \Big)^2
\sigma_j^2

\\ \text{expand square}

&= \frac{1}{R_0^2} \sum_j
\Big(
  \Re{e^{inwt_j}}^2
  - 2 \Re{e^{inwt_j}} \Re{r_n}
  + \Re{r_n}^2
\Big)
\; \sigma_j^2

\\ \text{take real part}

&= \frac{1}{R_0^2} \sum_j
\Big(
  \cos(nwt_j)^2
  - 2 \cos(nwt_j) \Re{r_n}
  + \Re{r_n}^2
\Big)
\; \sigma_j^2

\\ \text{trigonometric identity}

&= \frac{1}{R_0^2} \sum_j
\left(
  \frac{1 + \cos(2nwt_j)}{2}
  - 2 \cos(nwt_j) \Re{r_n}
  + \Re{r_n}^2
\right)
\; \sigma_j^2

\\ \text{factor out}

&= \frac{1}{2R_0^2} \sum_j
\left(
  1 + \cos(2nwt_j)
  - 4 \cos(nwt_j) \Re{r_n}
  + 2 \Re{r_n}^2
\right)
\; \sigma_j^2
\end{align*}
$$

### Imaginary part

$$
\begin{align*}
\Var{\Im{r_n}} &=

\\ \text{asuming independence}

&= \sum_j \left(\frac{\partial \Im{r_n}}{\partial X_j} \; \sigma_j \right)^2

\\ \text{similar as before}

&= \ldots

\\ \text{expand square}

&= \frac{1}{R_0^2} \sum_j
\Big(
  \Im{e^{inwt_j}}^2
  - 2 \Im{e^{inwt_j}} \Im{r_n}
  + \Im{r_n}^2
\Big)
\; \sigma_j^2

\\ \text{take imaginary part}

&= \frac{1}{R_0^2} \sum_j
\Big(
  \sin(nwt_j)^2
  - 2 \sin(nwt_j) \Im{r_n}
  + \Im{r_n}^2
\Big)
\; \sigma_j^2

\\ \text{trigonometric identity}

&= \frac{1}{R_0^2} \sum_j
\left(
  \frac{1 - \cos(2nwt_j)}{2}
  - 2 \sin(nwt_j) \Im{r_n}
  + \Im{r_n}^2
\right)
\; \sigma_j^2

\\ \text{factor out}

&= \frac{1}{2R_0^2} \sum_j
\left(
  1 - \cos(2nwt_j)
  - 4 \sin(nwt_j) \Im{r_n}
  + 2 \Im{r_n}^2
\right)
\; \sigma_j^2
\end{align*}
$$

### Covariance of real and imaginary parts

$$
\begin{align*}
\Cov{\Re{r_n}}{\Im{r_n}} &=

\\ \text{asuming independence}

&= \sum_j \frac{\partial \Re{r_n}}{\partial X_j} \frac{\partial \Im{r_n}}{\partial X_j} \; \sigma_j^2

\\ \text{similar as before}

&= \ldots

\\ \text{factor out}

&= \frac{1}{R_0^2} \sum_j
\Big( \Re{e^{inwt_j}} - \Re{r_n} \Big)
\Big( \Im{e^{inwt_j}} - \Im{r_n} \Big)
\, \sigma_j^2

\\ \text{expand product}

&= \frac{1}{R_0^2} \sum_j
\Big(
  \Re{e^{inwt_j}} \Im{e^{inwt_j}}
- \Re{e^{inwt_j}} \Im{r_n}
- \Im{e^{inwt_j}} \Re{r_n}
+ \Re{r_n} \Im{r_n}
\Big)
\; \sigma_j^2

\\ \text{take real and imaginary parts}

&= \frac{1}{R_0^2} \sum_j
\Big(
  \cos(nwt_j) \sin(nwt_j)
- \cos(nwt_j) \Im{r_n}
- \sin(nwt_j) \Re{r_n}
+ \Re{r_n} \Im{r_n}
\Big)
\; \sigma_j^2

\\ \text{trigonometric identity}

&= \frac{1}{R_0^2} \sum_j
\left(
  \frac{\sin(2nwt_j)}{2}
- \cos(nwt_j) \Im{r_n}
- \sin(nwt_j) \Re{r_n}
+ \Re{r_n} \Im{r_n}
\right)
\; \sigma_j^2
\end{align*}
$$

## Variance as a function of mean

$E[X_j] = \mu_j$
and
$\Var{X_j} = \sigma_j^2 = a \mu_j + b$

### Real part

$$
\begin{align*}
\Var{\Re{r_n}} &=

\\ \text{copying from above}

&= \frac{1}{2 \, R_0^2}
\sum_j
\left(
  1 + \cos(2nwt_j)
  - 4 \cos(nwt_j) \Re{r_n}
  + 2 \Re{r_n}^2
\right)
\; \sigma_j^2

\\ \text{parametrized variance}

&= \frac{1}{2 \, R_0^2}
\sum_j
\left(
  1 + \cos(2nwt_j)
  - 4 \cos(nwt_j) \Re{r_n}
  + 2 \Re{r_n}^2
\right)
\; (a \mu_j + b)

\\ \text{distribute}

&= \frac{1}{2 \, R_0^2} \left[
a \sum_j \mu_j
\left(
  1 + \cos(2nwt_j)
  - 4 \cos(nwt_j) \Re{r_n}
  + 2 \Re{r_n}^2
\right)
+
b \sum_j
\left(
  1 + \cos(2nwt_j)
  - 4 \cos(nwt_j) \Re{r_n}
  + 2 \Re{r_n}^2
\right)
\right]

\\ \text{sum}

&= \frac{1}{2 \, R_0^2} \left[
a
\left(
  R_0 + \Re{R_{2n}}
  - 4 \Re{R_n} \Re{r_n}
  + 2 R_0 \Re{r_n}^2
\right)
+
b
\left(
  N_b + 0
  - 4 \cdot 0 \Re{r_n}
  + 2 N_b \Re{r_n}^2
\right)
\right]

\\

&= \frac{1}{2 \, R_0^2} \left[
a
\left(
  R_0
  + R_0 \Re{r_{2n}}
  - 4 R_0 \Re{r_n}^2
  + 2 R_0 \Re{r_n}^2
\right)
+
b
\left(
  N_b
+ 2 N_b \Re{r_n}^2
\right)
\right]

\\

&= \frac{1}{2 \, R_0^2} \left[
a \, R_0 \left(1 + \Re{r_{2n}} - 2 \Re{r_n}^2 \right)
+
b \, N_b \left( 1 - 2 \Re{r_n}^2 \right)
\right]
\end{align*}
$$


### Imaginary part

$$
\begin{align*}
\Var{\Im{r_n}}

&= \frac{1}{2 \, R_0^2}
\sum_j
\left(
  1 - \cos(2nwt_j)
  - 4 \sin(nwt_j) \Im{r_n}
  + 2 \Im{r_n}^2
\right)
\; (a \mu_j + b)

\\

&= \frac{1}{2 \, R_0^2} \left[
a \, R_0 \left(1 - \Re{r_{2n}} - 2 \Im{r_n}^2 \right)
+
b \, N_b \left( 1 - 2 \Im{r_n}^2 \right)
\right]
\end{align*}
$$

### Covariance of real and imaginary parts

$$
\begin{align*}
\Cov{\Re{r_n}, \Im{r_n}}

&= \frac{1}{R_0^2} \sum_j
\left(
  \frac{\sin(2nwt_j)}{2}
- \cos(nwt_j) \Im{r_n}
- \sin(nwt_j) \Re{r_n}
+ \Re{r_n} \Im{r_n}
\right)
\; (a \mu_j + b)

\\

&= \frac{1}{R_0^2}
\left(
  \frac{a \Im{R_{2n}} + b \cdot 0}{2}
- (a \Re{R_n} + b \cdot 0) \Im{r_n}
- (a \Im{R_n} + b \cdot 0) \Re{r_n}
+ (a R_0 + b N_b) \Re{r_n} \Im{r_n}
\right)

\\

&= \frac{1}{R_0^2}
\left(
  \frac{a R_0 \Im{r_{2n}}}{2}
- a R_0 \Re{r_n} \Im{r_n}
- a R_0 \Im{r_n} \Re{r_n}
+ (a R_0 + b N_b) \Re{r_n} \Im{r_n}
\right)

\\

&= \frac{1}{R_0^2}
\left(
  \frac{a R_0 \Im{r_{2n}}}{2}
+ (b N_b - a R_0) \Re{r_n} \Im{r_n}
\right)
\end{align*}
$$
