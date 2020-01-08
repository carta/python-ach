from datetime import datetime

from ach.builder import AchFile


class TestBuilder:

    def test_add_batch_no_start_entry_counter(self):
        settings = {
            'company_id': '999999999',
            'company_name': 'CAULIFLOWER LTD',
            'immediate_dest': '123456789',
            'immediate_dest_name': 'DESTRO INC',
            'immediate_org': 'ORANG LLC',
            'immediate_org_name': 'ORANG LLC',
            'file_gen_datetime': datetime(2020, 1, 1)
        }

        entries = [
            {
                'type': '22',
                'routing_number': '234567890',
                'account_number': '3456789012',
                'amount': 45.67,
                'name': 'Nonce Cornelius',
                'id_number': '5555555555',
            }

        ]

        f = AchFile('A', settings)
        f.add_batch(std_ent_cls_code='PPD', batch_entries=entries)

        lines = f.render_to_string().split('\n')
        entry_line = lines[2].split()
        assert entry_line[len(entry_line) - 1] == '0123456780000001'

    def test_add_batch_using_start_entry_counter(self):
        settings = {
            'company_id': '999999999',
            'company_name': 'CAULIFLOWER LTD',
            'immediate_dest': '123456789',
            'immediate_dest_name': 'DESTRO INC',
            'immediate_org': 'ORANG LLC',
            'immediate_org_name': 'ORANG LLC',
            'file_gen_datetime': datetime(2020, 1, 1)
        }

        entries = [
            {
                'type': '22',
                'routing_number': '234567890',
                'account_number': '3456789012',
                'amount': 45.67,
                'name': 'Nonce Cornelius',
                'id_number': '5555555555',
            }

        ]

        f = AchFile('A', settings)
        f.add_batch(
            std_ent_cls_code='PPD',
            batch_entries=entries,
            start_entry_counter=77)

        lines = f.render_to_string().split('\n')
        entry_line = lines[2].split()
        assert entry_line[len(entry_line) - 1] == '0123456780000077'
