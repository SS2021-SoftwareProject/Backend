




def project_donate(project: Project, user_inst: User, amount: int, vote_enabled: bool):
    project_donate_register(project, user_inst)

    donations_sc = WEB3.eth.contract([...],'0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe') #vlt wenn möglich nicht hardcode

    tx_hash = donations_sc.functions.donate() \
        .buildTransaction(
        {
            'nonce': WEB3.eth.getTransactionCount(user_inst.publickeyUser),
            'from': user_inst.publickeyUser,
            'value': int(amount)
        })
    signed_tx = WEB3.eth.account.sign_transaction(tx_hash, private_key=user_inst.privatekeyUser)
    tx_hash2 = WEB3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = WEB3.eth.waitForTransactionReceipt(tx_hash2)
    if tx_receipt.status != 1:
        raise RuntimeError("SC Call failed!")

    processed_receipt = donations_sc.events.Donate().processReceipt(tx_receipt)
    milestone_sc_index = processed_receipt[0].args.milestoneId  # pylint:disable=protected-access

    return milestone_sc_index
