import collections
class Solution:
    def numUniqueEmails(self, emails: [str]) -> int:

        def clear(localname):
            localname = localname[0] + localname[1:].replace('.', '')
            if '+' in localname:
                localname = localname[:localname.index('+')-1]
            return localname


        count = 0
        dic = collections.defaultdict(set)
        for email in emails:
            localname,domainname = email.split('@')

            localname = clear(localname)
            if localname not in dic:
                dic[localname].add(domainname)
                count+=1
            else:
                if domainname not in dic[localname]:
                    dic[localname].add(domainname)
                    count+=1
        
        return count
    
class BestSolution:
    def numUniqueEmails(self, emails: '[str]') -> 'int':
        emails_set = set()
        for email in emails:
            [temp_local_name, domain_name] = email.split('@')
            [tmp_local_name, _, _] = temp_local_name.partition('+')
            local_name = tmp_local_name.replace('.', '')
            fixed_email = local_name + '@' + domain_name
            emails_set.add(fixed_email)
        return len(emails_set)

a = Solution()
print(a.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))