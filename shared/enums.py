from collections.abc import Sequence

from django.db import models


class BloodType(models.TextChoices):
    Amin = "A-"
    Apos = "A+"
    Omin = "O-"
    Opos = "O+"
    Bmin = "B-"
    Bpos = "B+"
    ABmin = "AB-"
    ABpos = "AB+"

    # Refrance: https://www.inovablood.org/donate-blood/ideal-donation-for-your-blood-type/
    @property
    def donates_to(self) -> Sequence["BloodType"]:
        return {
            self.Amin: [self.Amin, self.Omin],
            self.Apos: [
                self.Amin,
                self.Apos,
                self.Opos,
                self.Omin,
            ],
            self.Bmin: [self.Bmin, self.Omin],
            self.Bpos: [self.Bmin, self.Bpos, self.Opos, self.Omin],
            self.ABmin: [self.Amin, self.Omin, self.Bmin, self.ABmin],
            self.ABpos: [
                self.Amin,
                self.Apos,
                self.Opos,
                self.Omin,
                self.ABpos,
                self.ABmin,
                self.Bmin,
                self.Bpos,
            ],
            self.Opos: [self.Opos, self.Omin],
            self.Omin: [self.Omin],
        }[self]

    @property
    def receives_from(self) -> Sequence["BloodType"]:
        return {
            self.Apos: [self.Apos, self.ABpos],
            self.Amin: [self.Amin, self.ABmin, self.Apos, self.ABpos],
            self.Bpos: [self.Bpos, self.ABpos],
            self.Bmin: [self.Bmin, self.ABmin, self.Bpos, self.ABpos],
            self.Opos: [self.Opos, self.ABpos, self.Apos, self.Bpos],
            self.Omin: [
                self.Omin,
                self.ABmin,
                self.Amin,
                self.Bmin,
                self.Opos,
                self.ABpos,
                self.Apos,
                self.Bpos,
            ],
            self.ABpos: [self.ABpos],
            self.ABmin: [self.ABmin, self.ABpos],
        }[self]
