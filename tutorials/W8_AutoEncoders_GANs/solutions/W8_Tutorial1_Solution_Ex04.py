def rsample(phi, n_samples):
    """Sample z ~ q(z;phi)
    Ouput z is size [b,n_samples,K] given phi with shape [b,K+1]. The first K
    entries of each row of phi are the mean of q, and phi[:,-1] is the log
    standard deviation
    """
    b, kplus1 = phi.size()
    eps = torch.randn(b, n_samples, kplus1-1, device=phi.device)
    mu, sig = phi[:, :-1], phi[:,-1].exp()
    return eps*sig.view(b,1,1) + mu.view(b,1,kplus1-1)
