import sys
from p1 import decode
from p2 import get_key


def main():
    stu_id = sys.argv[1]
    with open(f'{stu_id}.txt', 'r') as fi:
        problems = fi.read().split('\n')
        p1_cipher, p1_key = problems[:2]
        p2_cipher1, p2_plain1, p2_cipher2 = problems[3:]

    p1_plain = decode(p1_cipher, p1_key)
    p2_key = get_key(p2_cipher1, p2_plain1)
    p2_plain2 = decode(p2_cipher2, p2_key)

    with open(f'{stu_id}_ans.txt', 'w') as fo:
        fo.write(f'{stu_id}\n')
        fo.write(f'{p1_plain}\n')
        fo.write(f'{p2_key}\n')
        fo.write(f'{p2_plain2}')


if __name__ == '__main__':
    main()
