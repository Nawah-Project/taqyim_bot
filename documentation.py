

class Documentation:
    def __init__(self):
        # الكلمات المتعلقة بالتوثيق
        documentation_keywords = [
            "توثيق", "التوثيق", "توثيقي", "التوثيقي",
            "موثّق", "موثق", "توثيقًا", "توثيقية"
        ]
        
        # الكلمات المتعلقة بالأسبوع
        week_keywords = [
            "الأسبوع", "الاسبوع", "أسبوع", "اسبوع",
            "الأسبوعي", "الاسبوعي", "أسبوعي", "اسبوعي"
        ]
        
        # اجمعهم في لستة واحدة
        self.required_keywords = documentation_keywords + week_keywords

    def check_documentation(self, message):
        """
        بيرجع True لو الرسالة فيها أي كلمة مفتاحية من التوثيق + الأسبوع
        """
        for keyword in self.required_keywords:
            if keyword in message:
                return True
        return False
