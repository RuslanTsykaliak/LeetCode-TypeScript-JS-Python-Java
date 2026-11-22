class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        uniqueEmails = set()

        for e in emails:
            local, domain = e.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            uniqueEmails.add((local, domain))
        return len(uniqueEmails)
