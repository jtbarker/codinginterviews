class Solution(object):
    def numUniqueEmails(self, emails):
        seen = set()
        for email in emails:
            local, _, domain = email.partition('@') #partition function is a handy way to split up a string on a specific pattern"
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)