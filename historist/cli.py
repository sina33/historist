import argparse
from historist import insert_event
from historist import print_table_contents
from historist import delete_tables
from historist import insert_batch_file
import os
import sys


def histopush():
    exec_cmd("historist " + "-i " + " ".join(sys.argv[1:]))
    # parser = argparse.ArgumentParser()
    # parser.add_argument("action", help="the action you took")
    # parser.add_argument("value", help="how much of that action you did")
    # args = parser.parse_args()
    # insert_event(args.action, args.value)


def historist():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--show', action="store_true")
    parser.add_argument('-i', '--insert', nargs=2, metavar=('action', 'value'), default=[None])
    parser.add_argument('--delete-database', action="store_true", help='delete your entire database')
    parser.add_argument('-bi', '--batch-input', nargs=1, metavar='filename', help='batch input from file', default=[])
    # parser.add_argument('--pop', action="store_true", help='remove the last entry from your database')
    args = parser.parse_args()
    if args.show:
        print_table_contents('actions')
        print_table_contents('events')
    elif len(args.insert) == 2:
        insert_event(args.insert[0], args.insert[1])
    elif args.delete_database:
        delete_tables()
    elif len(args.batch_input) > 0:
        insert_batch_file(args.batch_input[0])
    else:
        print "Welcome to historist-0.1.0.dev2"


def histoplay():
    if len(sys.argv) > 1:
        exec_cmd("historist " + "-o " + " ".join(sys.argv[1:]))
    else:
        exec_cmd("historist -s")
        # parser = argparse.ArgumentParser()
        # parser.add_argument('action', help="the action which you want to see it's history")
        # args = parser.parse_args()
        # print args.action
        # print_table_contents('actions')
        # print_table_contents('events')


def exec_cmd(cmd):
    print "cmd: " + cmd
    os.system(cmd)


if __name__ == "__main__":
    historist()