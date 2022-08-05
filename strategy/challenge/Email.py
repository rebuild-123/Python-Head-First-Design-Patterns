from ShareStrategy import ShareStrategy


class Email(ShareStrategy):
    def share(self) -> None:
        print("I'm emailing the photo")