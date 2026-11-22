class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        uniqueEmails = set()

        for e in emails:
            # Build in functions
            # local, domain = e.split("@")
            # local = local.split("+")[0]
            # local = local.replace(".", "")

            # Iterative while loop
            i, local = 0, ""
            while e[i] not in ["@", "+"]:
                if e[i] != ".":
                    local += e[i]
                i += 1

            while e[i] != "@":
                i += 1
            domain = e[i + 1 :]

            uniqueEmails.add((local, domain))
        return len(uniqueEmails)
