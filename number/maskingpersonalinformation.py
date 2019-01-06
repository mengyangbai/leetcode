class Solution(object):
    def convert_phone(self, phone):
        phone = phone.strip().replace(' ', '').replace('(', '').replace(')', '').replace('-', '').replace('+', '')
        if len(phone) == 10:
            return "***-***-" + phone[-4:]
        else:
            return "+" + '*' * (len(phone) - 10) + "-***-***-" + phone[-4:]

    def convert_email(self, email):
        email = email.lower()
        first_name, host = email.split('@')
        return first_name[0] + '*****' + first_name[-1] + '@' + host

    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        return self.convert_email(S) if '@' in S else self.convert_phone(S)