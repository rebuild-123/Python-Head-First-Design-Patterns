class Zone:
    displayName: str
    offset: int = 0
    
    def getDisplayName(self) -> str:
        return self.displayName
    
    def getOffset(self) -> int:
        return self.offset