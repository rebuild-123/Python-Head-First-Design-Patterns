from ShareStrategy import ShareStrategy


class Social(ShareStrategy):
    def share(self) -> None:
        print("I'm posting the photo on social media")