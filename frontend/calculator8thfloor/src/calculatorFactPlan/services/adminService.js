class AdminService {
    constructor() {
      this.isAdmin = false;
    }
  
    setAdmin(isAdmin) {
      this.isAdmin = isAdmin;
      localStorage.setItem('isAdmin', isAdmin.toString());
    }
  
    getAdmin() {
      const isAdminString = localStorage.getItem('isAdmin');
      return isAdminString === 'true';
    }
  
    clearAdminStatus() {
      this.isAdmin = false;
      localStorage.removeItem('isAdmin');
    }
  }
  
  export default new AdminService();