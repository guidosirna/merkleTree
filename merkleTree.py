import hashlib

class MerkelTreeHash(object):

    def __init__(self):

    def find_merkel_hash(self, file_hashes):

        blocks = []

        if not file_hashes:
            raise ValueError('Missing required file hashes for computing merkel tree hash.')

        for m in sorted(file_hashes):
            blocks.append(m)

        list_len = len(blocks)
        while list_len % 2 != 0:
            blocks.extend(blocks[-1:])
            list_len = len(blocks)

        secondary = []
        for k in [blocks[x:x + 2] for x in xrange(0, len(blocks), 2)]:
            hasher = hashlib.sha256()
            hasher.update(k[0] + k[1])
            secondary.append(hasher.hexdigest())

        if len(secondary) == 1:
            # returning just the first 64 characters
            return secondary[0][0:64]
        else:
            return self.find_merkel_hash(secondary)

        
if __name__ == '__main__':

    import uuid

    file_hashes = []

    for i in range(0, 13):
        file_hashes.append(str(uuid.uuid4().hex))

    print('Finding the merkel tree hash of {0} random hashes.'.format(len(file_hashes)))

    cls = MerkelTreeHash()
    mk = cls.find_merkel_hash(file_hashes)
    print('The merkel tree hash of the hashes below is : {0}'.format(mk))
    print('...')
    print(file_hashes)
    
