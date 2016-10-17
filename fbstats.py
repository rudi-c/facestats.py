#!/usr/bin/python

import collections
import sys

from bs4 import BeautifulSoup
from message_thread import read_message_thread

def get_soup(filename):
    f = open(filename, 'r')
    contents = f.read()
    return BeautifulSoup(contents, 'lxml')

def thread_statistics(thread):
    print "[In conversation with %s]" % thread.name
    for author, (msg_count, word_count, words_per_msg) in thread.tally_messages().iteritems():
        print ("    %s: (%d messages, %d words, %.1f words/message)" %
               (author, msg_count, word_count, words_per_msg))

    blocks = thread.message_blocks()
    block_sizes = [len(block) for block in blocks]
    median_size = block_sizes[len(block_sizes)/2]
    print ("    Total of %d message blocks, median of %d messages" %
           (len(blocks), median_size))

    block_starters = [block[0].author for block in blocks]
    starter_counts = collections.Counter(block_starters)

    for author, count in starter_counts.iteritems():
        print ("    Conversations started by %s: %d (%.0f%%)" %
               (author, count, float(count) / len(blocks) * 100))

def main(argv):
    print "Reading message history..."
    soup = get_soup(argv[0])
    print "Loaded message history."

    full_name = soup.find("h1").get_text().strip()
    thread_nodes = soup.find_all("div", class_="thread")

    threads = []
    for thread_node in thread_nodes:
        thread = read_message_thread(full_name, thread_node)
        if thread is not None:
            threads.append(thread)

    threads = sorted(threads, key=lambda thread: len(thread.messages))

    for thread in threads:
        thread_statistics(thread)

    # print soup.prettify(encoding='utf-8')

if __name__ == "__main__":
   main(sys.argv[1:])
