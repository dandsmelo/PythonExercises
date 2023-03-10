{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN9Gc5NeNvjIY3u0DndPo2Y"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "Exercício 1001"
      ],
      "metadata": {
        "id": "VNiJZ4oG1_BW"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1lQLGm94r8Zm",
        "outputId": "f89cebef-d6c0-4edf-c024-35003eda5a71"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "15\n",
            "-7\n",
            "X = 8\n"
          ]
        }
      ],
      "source": [
        "A = int(input())\n",
        "B = int(input())\n",
        "X = A + B \n",
        "\n",
        "print(\"X = %d\" % X)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Exercício 1002"
      ],
      "metadata": {
        "id": "jFWdueNM15nK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "R = float(input())\n",
        "n = 3.14159\n",
        "A = n*R**2\n",
        "\n",
        "print(\"A=%.4f\" % A)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K87vo8Byzpei",
        "outputId": "d65b11b6-1c52-498c-9d93-63fe34cdb5a5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2.00\n",
            "A=12.5664\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Exercício 1003"
      ],
      "metadata": {
        "id": "nIyWLo-S3YuP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "A = int(input())\n",
        "B = int(input())\n",
        "SOMA = A + B\n",
        "print(\"SOMA = %d\" % SOMA)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tJy8TwQm2Ms1",
        "outputId": "98338e24-f2f9-4aaa-80dd-cca7a3d8d462"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "30\n",
            "10\n",
            "SOMA = 40\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Exercício 1004"
      ],
      "metadata": {
        "id": "o8DvLBpv3pYE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "A = int(input())\n",
        "B = int(input())\n",
        "p = A * B\n",
        "print (\"PROD = %d\" % p)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tu-4ZLtE3sHz",
        "outputId": "2740471e-f118-4349-cb4b-47af6ec5167d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "9\n",
            "PROD = 0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "1005"
      ],
      "metadata": {
        "id": "y3_3mHy_4jKg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "A = float(input())\n",
        "B = float(input())\n",
        "m = (A*3.5 + B*7.5)/11\n",
        "print(\"MEDIA = %.5f\" % m)"
      ],
      "metadata": {
        "id": "5QlWGzTO4o50",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2be30a43-fecb-4bc5-ba98-f1be76770f41"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10.0\n",
            "10.0\n",
            "MEDIA = 10.00000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "1006"
      ],
      "metadata": {
        "id": "e2KVzLuEmzxB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "A = float(input())\n",
        "B = float(input())\n",
        "C = float(input())\n",
        "m = (A*2+B*3+C*5)/10\n",
        "print(\"MEDIA = %.1f\" % m)"
      ],
      "metadata": {
        "id": "8Ztx0wksm1sr",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fe943bf3-b53e-4dc3-8fc0-1560a8a2e5be"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10.0\n",
            "10.0\n",
            "5.0\n",
            "MEDIA = 7.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "1007"
      ],
      "metadata": {
        "id": "FNylJlmRgCAL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "A = int(input())\n",
        "B = int(input())\n",
        "C = int(input())\n",
        "D = int(input())\n",
        "df = A*B - C*D\n",
        "print(\"DIFERENCA = %d\" % df)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tUu90rf8gDxo",
        "outputId": "a01c5ffc-6a3a-415d-c0ca-af20ce1b0f3b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n",
            "6\n",
            "-7\n",
            "8\n",
            "DIFERENCA = 86\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "1008"
      ],
      "metadata": {
        "id": "SPWYW-5Nsslt"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "F = int(input())\n",
        "H = int(input())\n",
        "S = float(input())\n",
        "SM = H*S\n",
        "print(\"NUMBER = %d\" % F)\n",
        "print(\"SALARY = U$ %0.2f\" % SM)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "swhQB9tMst4_",
        "outputId": "6b3f6838-1a08-459b-aaec-efb52b3c6eb4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "6\n",
            "145\n",
            "15.55\n",
            "NÚMERO = 6\n",
            "SALÁRIO = U$ 2254.75\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "1009\n"
      ],
      "metadata": {
        "id": "2KRDSlG9wMhM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "N = str(input())\n",
        "S = float(input())\n",
        "V = float(input())\n",
        "SF = S+V*0.15\n",
        "print(\"TOTAL = R$ %0.2f\" % SF)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VZVo_GDcwPaz",
        "outputId": "3fabd973-b40c-4bde-a464-05437b93852b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mangojata\n",
            "1700.00\n",
            "1230.50\n",
            "TOTAL = R$ 1884.58\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "1010"
      ],
      "metadata": {
        "id": "q_ANe0w30Bev"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "p1 = (input())\n",
        "p2 = (input())\n",
        "list1 = p1.split(\" \")\n",
        "list2 = p2.split(\" \")\n",
        "p1 = float(list1[2])\n",
        "u1 = int(list1[1])\n",
        "p2 = float(list2[2])\n",
        "u2 = int(list2[1])\n",
        "v = u1*p1+u2*p2\n",
        "print(\"VALOR A PAGAR: R$ %0.2f\" % v)"
      ],
      "metadata": {
        "id": "FVsHzXCL0C0v",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "14312373-78c6-4886-88d9-e0ceea6a0e43"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 1 15.10\n",
            "2 1 15.10\n",
            "VALOR A PAGAR = 30.20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "1011"
      ],
      "metadata": {
        "id": "tyvWieEebwag"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "r = float(input())\n",
        "pi =  3.14159\n",
        "v = (4/3) * pi * r**3\n",
        "print(\"VOLUME = %.3f\" % v)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Bof3ri33bxfN",
        "outputId": "fc10f78d-a6ef-47e2-affc-8df5c2eb037e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1523\n",
            "VOLUME = 14797486501.627\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "1012"
      ],
      "metadata": {
        "id": "fpnpASQWO6Ft"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "abc = (input())\n",
        "list1 = abc.split(\" \")\n",
        "A = float(list1[0])\n",
        "B = float(list1[1])\n",
        "C = float(list1[2])\n",
        "pi = 3.14159\n",
        "T = (A*C)/2\n",
        "CO = pi*C**2\n",
        "TP = (A+B)*(C/2)\n",
        "Q = B*B\n",
        "R = A*B\n",
        "print(\"TRIANGULO: %.3f\" % T)\n",
        "print(\"CIRCULO: %.3f\" % CO)\n",
        "print(\"TRAPEZIO: %.3f\" % TP)\n",
        "print(\"QUADRADO: %.3f\" % Q)\n",
        "print(\"RETANGULO: %.3f\" % R)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OJ8J6efWO7E_",
        "outputId": "133cb464-954a-4f9c-a24d-db5f85b2a78c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.0 4.0 5.2\n",
            "TRIANGULO: 7.800\n",
            "CIRCULO: 84.949\n",
            "TRAPEZIO: 18.200\n",
            "QUADRADO: 16.000\n",
            "RETANGULO: 12.000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "teste 1012"
      ],
      "metadata": {
        "id": "A0kK8aPlRf3t"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "ABC = input().split()\n",
        "ABC = float(A), float(B), float(C)\n",
        "pi = 3.14159\n",
        "T= A*C/2\n",
        "CO = pi*C**2\n",
        "TR = (A+B)*(C/2)\n",
        "Q = B*B\n",
        "R = A*B\n",
        "print (\"TRIANGULO: %.3f\" % T)\n",
        "print (\"CIRCULO: %.3f\" % CO)\n",
        "print (\"TRAPEZIO: %.3f\" % TR)\n",
        "print (\"QUADRADO: %.3f\" % Q)\n",
        "print (\"RETANGULO: %.3f\" % R)"
      ],
      "metadata": {
        "id": "RRRvvRkTkmF8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "affaa3c3-498a-47b3-828e-2b1bcd6d5ccf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.0 4.0 5.2\n",
            "TRIANGULO: 7.800\n",
            "CIRCULO: 84.949\n",
            "TRAPEZIO: 18.200\n",
            "QUADRADO: 16.000\n",
            "RETANGULO: 12.000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "1013"
      ],
      "metadata": {
        "id": "LXVtWSOCgYTG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = int(input())\n",
        "b = int(input())\n",
        "s = int(input())\n",
        "mab = "
      ],
      "metadata": {
        "id": "1JtpV2-sgZkY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "1014"
      ],
      "metadata": {
        "id": "Ew7dL3GBmseC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x = int(input())\n",
        "y = float(input())\n",
        "cm = x/y\n",
        "print(\"%.3f km/l\" % cm)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LNFFZsTjmvHo",
        "outputId": "004fcf16-a55e-463f-ccdf-5bb0bfa72d96"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4554\n",
            "464.6\n",
            "9.802 km/l\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "1035"
      ],
      "metadata": {
        "id": "3osCMuHLFZVH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "v = (input())\n",
        "list1 = v.split(\" \")\n",
        "A = int(list1[0])\n",
        "B = int(list1[1])\n",
        "C = int(list1[2])\n",
        "D = int(list1[3])\n",
        "if ( B>C and D>A and C+D>A+B and C>=0 and D>=0 and A%2 == 0):\n",
        "  print(\"Valores aceitos\")\n",
        "else:\n",
        "  print(\"Valores nao aceitos\")"
      ],
      "metadata": {
        "id": "y2Xz8o1rFbc1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a3122a54-4960-42a4-b033-c524ccb038e7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2 3 2 6\n",
            "Valores aceitos\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "1038"
      ],
      "metadata": {
        "id": "Ob-dOrecbC7T"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "cq = input().split(\" \")\n",
        "cq = int(X), int(Y)\n",
        "X = "
      ],
      "metadata": {
        "id": "eKanXFxnbFjg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "1050"
      ],
      "metadata": {
        "id": "XYfkXCwdtTNo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "number = int(input())\n",
        "if number = 61:\n",
        "  "
      ],
      "metadata": {
        "id": "Ovfr9UQvtSEJ"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}