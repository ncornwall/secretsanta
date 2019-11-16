import random

class BadSecretSantaError(Exception):
   pass

class HoHoHo:
    
    def __init__(self):
        self.myfamily = ["Tom", "Leanna", "Mom", "Dad", "Talia", "Pat"]
        self.couples = [{"Tom", "Leanna"}, {"Mom", "Dad"}, {"Talia", "Pat"}]
        self.secret_santa_assignments = {}

    def generate_secret_santa(self):
        while len(self.secret_santa_assignments) < 6:
            randomGiftGiver = random.randint(0, 5)
            randomGiftRecipient = random.randint(0, 5)

            if (self.is_good_assignment(randomGiftGiver, randomGiftRecipient)):
                self.secret_santa_assignments[self.myfamily[randomGiftGiver]] = self.myfamily[randomGiftRecipient]
        
        self.check_no_one_left_out_of_secret_santa()

        print("Ho Ho Ho")

    def check_no_one_left_out_of_secret_santa(self):
        everyone_is_getting_a_gift = all(x in self.secret_santa_assignments.values() for x in self.myfamily)
        everyone_is_giving_a_gift = all(x in self.secret_santa_assignments.keys() for x in self.myfamily)

        if (len(self.secret_santa_assignments) != 6 
            or not everyone_is_getting_a_gift 
            or not everyone_is_giving_a_gift):
            raise BadSecretSantaError("Someone will be sad at Christmas!")

    def is_good_assignment(self, gifter, giftee):
        # don't give presents to yourself
        if gifter == giftee:
            return False
        # someone else is already giving this person a gift
        if self.myfamily[giftee] in self.secret_santa_assignments.values():
            return False
        # avoid couples
        if {self.myfamily[gifter], self.myfamily[giftee]} in self.couples:
            return False
        return True

    def make_secret_santa_emails(self):
        print("Creating email text file attachments")
        for k, v in self.secret_santa_assignments.items():
            with open(f"{k}.txt", 'w+') as f:
                f.write("🎅 🎄 ❄️ ☃️\n")
                f.write(f"Hello {k},\n")
                f.write(f"Your secret santa assignee is {v}!\n")
                f.write(f"Please get this person a gift 🎁!\n")
                f.write(f"✨Ho Ho Ho from Santa! ✨")

def main():
    hohoho = HoHoHo()
    hohoho.generate_secret_santa()
    hohoho.make_secret_santa_emails()

if __name__ == "__main__":
    main()
