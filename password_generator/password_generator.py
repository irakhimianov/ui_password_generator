import secrets
from enum import IntEnum
from math import log2
from random import randint, choices
from string import ascii_uppercase, ascii_lowercase, digits, punctuation


class StrengthToEntropy(IntEnum):
    """
    Password classification by entropy
    """
    Pathetic = 0
    Weak = 30
    Good = 50
    Strong = 70
    Excellent = 120


class PasswordGenerator:
    def __init__(self,
                 length: int = 0,
                 add_upper: bool = False,
                 add_lower: bool = False,
                 add_digits: bool = False,
                 add_punct: bool = False
                 ):
        self.length = length
        self.add_upper = add_upper
        self.add_lower = add_lower
        self.add_digits = add_digits
        self.add_punct = add_punct

    @property
    def alphabet(self) -> str:
        return self._get_alphabet()

    @property
    def entropy(self) -> float:
        return round(self._get_entropy(), 2)

    @property
    def strength(self) -> str:
        result = ''
        for strength in StrengthToEntropy:
            if self.entropy >= strength.value:
                result = f'{strength.name}'
        return result

    @property
    def password(self) -> str:
        if not self._is_valid():
            return ''
        return self._generate_password()

    @staticmethod
    def random_password(*, min_length: int = 6, length: int = 0):
        if not length:
            length = randint(min_length, 20)
        strength = list(map(bool, choices([0, 1], k=4)))
        random_pass = PasswordGenerator(length, *strength).password
        while not random_pass:
            random_pass = PasswordGenerator(length, *strength).password
        return random_pass

    def _get_alphabet(self) -> str:
        if not any((self.add_punct, self.add_digits, self.add_lower, self.add_upper)):
            return ''
        alphabet = ascii_uppercase * self.add_upper + \
                   ascii_lowercase * self.add_lower + \
                   digits * self.add_digits + \
                   punctuation * self.add_punct
        return alphabet

    def _get_entropy(self) -> float:
        if not self._is_valid():
            return 0.0
        return self.length * log2(len(self.alphabet))

    def _generate_password(self) -> str:
        if not self._is_valid():
            return ''
        return ''.join(secrets.choice(self.alphabet) for _ in range(self.length))

    def _is_valid(self) -> bool:
        if not self.length or not self.alphabet:
            return False
        return True
