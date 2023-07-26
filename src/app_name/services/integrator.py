from typing import List, Dict


class IntegratorService:
    """
        This service consists of some methods that helps us to get user detail with his or her pinfl
    """

    async def get_rejected_job_offers(self, pinfl: int) -> Dict:
        """
            This method counts the number of rejected job offers
        """
        data = [
            {
                "PINFL": 6253529283322,
                "MEHNATGA LAYOQOT": "yes",
                "6 OY ICHIDA MUJORAT QILGANLIK": "yes",
                "HISOBDA TURGANLIK": "yes",
                "RAD QILGANLIK": 1,
                "UZINI BAND QILGANLIK": "no",
                "JAMOAT ISHCHISI": "no"
            }
        ]
        """
            [
            ]
        """
        return data


integrator = IntegratorService()
